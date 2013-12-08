from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from mongoengine import ValidationError

from annotate.models import AnnotatedDoc
from annotate.forms import AnnotatedDocumentCreationForm

def index(request):
    ctx = {}
    return render_to_response(
        "annotate/index.html", RequestContext(request, ctx))

def new(request):
    form_class = AnnotatedDocumentCreationForm
    form = form_class()
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            title = form.cleaned_data['title']
            content = content.split("\r\n\r\n")
            text = [{'anot':segment, 'content':"Annotate me"} for segment in content]
            doc = AnnotatedDoc(text=text, title=title)
            doc.save()
            return HttpResponseRedirect(reverse("edit_annotateddoc", args=[doc.id]))

    ctx = {
        'form': form
    }
    return render_to_response(
        "annotate/new.html", RequestContext(request, ctx))

@csrf_exempt # FIXME: to be removed soon
def post(request):
    if not request.POST or not "doc" in request.POST:
        response = {"error": "Invalid request"}
    else:
        try:
            text = simplejson.loads(request.POST["doc"])
            doc_hash = request.POST.get("doc_hash")
        except ValueError:
            response = {"error": "Invalid document"}
        else:
            try:
                doc = AnnotatedDoc.objects.get(id=doc_hash)
                doc.text = text
            except AnnotatedDoc.DoesNotExist:
                doc = AnnotatedDoc(text=text)
            except ValidationError:
                doc = AnnotatedDoc(text=text)
            except Exception, e:
                raise Exception, "UH OH: %s" % e
            finally:
                doc.save()
            response = {"success": True, "doc": str(doc.id)}
    return HttpResponse(
        simplejson.dumps(response), content_type="application/json")

def get(request, doc_hash):
    if not request.GET or not doc_hash:
        response = {"error": "Invalid request"}
    try:
        doc = AnnotatedDoc.objects.get(id=doc_hash)
    except (ValidationError, AnnotatedDoc.DoesNotExist):
        response = {"error": "Does not exist"}
    else:
        response = {"success": True, "text": doc.text}

    return HttpResponse(
        simplejson.dumps(response), content_type="application/json")

def edit(request, doc_hash):
    try:
        doc = AnnotatedDoc.objects.get(id=doc_hash)
    except (ValidationError, AnnotatedDoc.DoesNotExist):
        raise Http404

    ctx = {'doc_hash': doc_hash,
           'doc': doc
        }
    return render_to_response(
        "annotate/edit.html", RequestContext(request, ctx))

def list(request):
    docs = AnnotatedDoc.objects.all()
    ctx = {
        "docs" : docs
        }
    return render_to_response(
        "annotate/list.html", RequestContext(request, ctx))
