from data.models import Category, Workflow
import os
import django
from data.management.commands.populate import Command, CATEGORY, WORKFLOW
from django.core.management.base import BaseCommand

from random import randint


os.environ.setdefault('DJANGO SETTINGS MODULE', 'projectName.settings')
django.setup()
        
# check if there is a user with id=10
# otherwise create new user

class Command(BaseCommand):

    def handle(self, *args, **options):
        """Executed by default. It implements the queries from the assignment
        Author: Francisco de Vicente Lana

        Args:
            self: class argument.
            args: optional.
            options: optional.

        Returns:
            -
        """
        # CATEGORY 1
        name = 'category 1'
        self.c1 = Category.objects.get_or_create(name = name)[0]

        # CATEGORY 2
        name = 'category 2'
        self.c2 = Category.objects.get_or_create(name = name)[0]

        # WF 11, 12 AND 13
        self.init_wf(range(11,14), self.c1)

        # WF 21, 22 AND 23
        self.init_wf(range(21,24), self.c2)

        # QUERY 1 - List of object related to a concrete Category
        print "QUERY 1 RESULTS:"
        query_result = self.listByCategory(self.c1)
        print query_result

        # QUERY 2 - Given a workflow slug returns its associated Category
        print "QUERY 2 RESULTS:"
        query_result = self.catFromWorkflow("workflow-1")
        print query_result 

        # QUERY 3 - Reusing the previous one

        # We change 10 by 100 because 10 actually exist with our implementation of populate
        print "QUERY 3 RESULTS:"
        query_result = self.catFromWorkflow("workflow-100")


    def init_wf(self, list_wf, cat):
        """If they does not exist, this function create some workflows.
        Author: Francisco de Vicente Lana

        Args:
            self: class argument.
            list_wf: list of integers for workflow's names.
            cat: categorie of the workflows.

        Returns:
            -
        """
        for wfi in list_wf:
            name = 'workflow {}'.format(wfi)
            lista_ip = []
            for x in range(4):
                lista_ip.append(str(randint(0, 255)))
            ip = '.'.join(lista_ip)
            wf = None
            try: 

                wf = Workflow.objects.get(name = name)

            except: 
                wf = Workflow(name = name,  client_ip = ip)
                wf.json = self.getJson()
                wf.save()
                wf.category.add(cat)
                wf.save()

    def listByCategory(self, cat):
        """It lists workflows asociated with a certain categorie, if they exists.
        Author: Francisco de Vicente Lana

        Args:
            self: class argument.
            cat: the categorie of each workflow.

        Returns:
            the list of workflows with the cat categorie or none
        """
        L = Workflow.objects.filter(category = cat)
        
        if L.exists():
            return L.all()
        else: 
            return None    
    
    def catFromWorkflow(self, slug):
        """It shows the categorie asociated with a certain workflow.
        Author: Francisco de Vicente Lana

        Args:
            self: class argument.
            slug: the slug of the workflow.

        Returns:
            the categorie of this workflow
        """
        try: 
            wf = Workflow.objects.get(slug = slug)
            return wf.category.all()[0]
        except: 
            print "Workflow named " + slug + " does not exist"
            return None

    def getJson(self):
        """Provides a json example for testing.
        Author: given

        Args:
            self: class argument.

        Returns:
            The json example.
        """
        return """[
    {
        "object.className": "ProtImportMovies",
        "object.id": "2",
        "object.label": "import movies",
        "object.comment": "\\n",
        "runName": null,
        "runMode": 0,
        "importFrom": 0,
        "filesPath": "",
        "filesPattern": "Falcon*.mrcs",
        "copyFiles": false,
        "acquisitionWizard": null,
        "voltage": 300.0,
        "sphericalAberration": 2.0,
        "amplitudeContrast": 0.1,
        "magnification": 39548,
        "samplingRateMode": 0,
        "samplingRate": 3.54,
        "scannedPixelSize": 14.0,
        "gainFile": null
    },
    {
        "object.className": "ProtMovieAlignment",
        "object.id": "40",
        "object.label": "movie alignment",
        "object.comment": "\\n",
        "runName": null,
        "runMode": 0,
        "cleanMovieData": true,
        "alignMethod": 0,
        "alignFrame0": 0,
        "alignFrameN": 0,
        "doGPU": false,
        "GPUCore": 0,
        "winSize": 150,
        "sumFrame0": 0,
        "sumFrameN": 0,
        "cropOffsetX": 0,
        "cropOffsetY": 0,
        "cropDimX": 0,
        "cropDimY": 0,
        "binFactor": 1,
        "extraParams": "",
        "hostName": "localhost",
        "numberOfThreads": 4,
        "numberOfMpi": 1,
        "inputMovies": "2.__attribute__outputMovies"
    },
    {
        "object.className": "ProtCTFFind",
        "object.id": "82",
        "object.label": "ctffind4",
        "object.comment": "\\n",
        "runName": null,
        "runMode": 0,
        "recalculate": false,
        "sqliteFile": null,
        "ctfDownFactor": 1.0,
        "useCftfind4": true,
        "astigmatism": 100.0,
        "findPhaseShift": false,
        "lowRes": 0.05,
        "highRes": 0.35,
        "minDefocus": 0.5,
        "maxDefocus": 4.0,
        "windowSize": 256,
        "hostName": "localhost",
        "numberOfThreads": 4,
        "numberOfMpi": 1,
        "inputMicrographs": "40.__attribute__outputMicrographs"
    },
    {
        "object.className": "EmanProtBoxing",
        "object.id": "369",
        "object.label": "eman2 - boxer",
        "object.comment": "",
        "runName": null,
        "runMode": 0,
        "inputMicrographs": "40.__attribute__outputMicrographs"
    },
    {
        "object.className": "ProtUserSubSet",
        "object.id": "380",
        "object.label": "3mics",
        "object.comment": "",
        "runName": null,
        "runMode": 0,
        "other": null,
        "sqliteFile": "Runs/000082_ProtCTFFind/ctfs_selection.sqlite,",
        "outputClassName": "SetOfMicrographs",
        "inputObject": "82.__attribute__outputCTF"
    },
    {
        "object.className": "XmippProtParticlePicking",
        "object.id": "420",
        "object.label": "xmipp3 - manual picking",
        "object.comment": "",
        "runName": null,
        "runMode": 0,
        "memory": 2.0,
        "inputMicrographs": "40.__attribute__outputMicrographs"
    },
    {
        "object.className": "XmippProtExtractParticles",
        "object.id": "449",
        "object.label": "extract 3 mics",
        "object.comment": "\\n",
        "runName": null,
        "runMode": 0,
        "micsSource": 0,
        "boxSize": 64,
        "doSort": false,
        "rejectionMethod": 0,
        "maxZscore": 3,
        "percentage": 5,
        "doRemoveDust": true,
        "thresholdDust": 3.5,
        "doInvert": true,
        "doFlip": false,
        "doNormalize": true,
        "normType": 2,
        "backRadius": -1,
        "hostName": "localhost",
        "numberOfThreads": 1,
        "numberOfMpi": 1,
        "ctfRelations": "82.__attribute__outputCTF",
        "inputCoordinates": "123.__attribute__outputCoordinates",
        "inputMicrographs": "369.outputMicrographs"
    },
    {
        "object.className": "XmippParticlePickingAutomatic",
        "object.id": "517",
        "object.label": "xmipp3 - auto-picking",
        "object.comment": "",
        "runName": null,
        "runMode": 0,
        "micsToPick": 0,
        "memory": 2.0,
        "hostName": "localhost",
        "numberOfThreads": 1,
        "numberOfMpi": 1,
        "xmippParticlePicking": "420"
    }
]"""
