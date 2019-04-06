# populate database
# The name of the script is the name of the custom command,
# so let's call it populate.py.
#
# execute python manage.py populate

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

import django
import random

django.setup()

from data.models import Category, Workflow
from random import randint

#models
CATEGORY = 'category'
USER = 'user'
WORKFLOW = 'workflow'
# The name of this class is not optional must  be Command
# otherwise manage.py will not process it properly
class Command(BaseCommand):
    #  args = '<-no arguments>'
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = 'This scripts populates de workflow database, no arguments needed.' \
           'Execute it with the command line python manage.py populate'

    def getParragraph(self, init, end):
        # getParragraph returns a parragraph, useful for testing
        if end > 445:
            end = 445
        if init < 0:
            init = 0
        return """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum."""[init:end]

    # handle is another compulsory name, This function will be
    # executed by default
    def handle(self, *args, **options):
        """Executed by default. It clears the database and after that
            populates it with five categories and 13 workflows.
        Author: Emilio Cuesta Fernandez

        Args:
            self: class argument.
            args: optional.
            options: optional.

        Returns:
            -
        """
        self.cleanDatabase()
        self.addCategory(5) # add 5 categories
        self.addWorkflow(13) # add 13 workflows


    def cleanDatabase(self):
        """It cleans the database by deleting all categorie and workflow objects.
        Author: Emilio Cuesta Fernandez

        Args:
            self: class argument.

        Returns:
            -
        """
        # delete all
        # workflows and categories
        Category.objects.all().delete()
        Workflow.objects.all().delete()
        pass

    def addCategory(self, noCategories):
        """This function adds a certain number of categories to the database.
        Author: Emilio Cuesta Fernandez

        Args:
            self: class argument.
            noCategories: number of categories to be added.

        Returns:
            -
        """
        # create 5 categories <<<<<<<<<<<<<<<<<<<<<<<
        # baseName, call objects
        # print Category.objects.all()
        for i in range(noCategories):
            nombre = "cat " + str(i)
            c = Category.objects.get_or_create(name = nombre)[0]
            c.tooltip = self.getParragraph(randint(1, 20), randint(50, 120))
            c.save()


    def addWorkflow(self, noWorkflows):
        """ it creates some workflows and assign them to random categories.
            Do not assign the sameworkflow to two or more categories.
        Author: Emilio Cuesta Fernandez

        Args:
            self: class argument.
            noWorkflows: number of workflows to be added.

        Returns:
            -
        """
        # create 13 workflows  <<<<<<<<<<<<<<<<<<<<<<
        # assign them to random categories
        # do not assign the sameworkflow to two o mote
        # categories
        # add apropriate code
        # create fake json
        json = self.getJson()
        longitud = len(Category.objects.all())

        for i in range(noWorkflows):
            nombre = "workflow " + str(i)
            lista_ip = []
            for x in range(4):
                lista_ip.append(str(randint(0, 255)))
            ip = '.'.join(lista_ip)

            w = Workflow.objects.get_or_create(name = nombre, client_ip = ip)[0]
            w.description = self.getParragraph(randint(1, 20), randint(50, 100))
            w.versionInit = self.getParragraph(randint(1, 10), randint(20, 120))

            cats = Category.objects.all()
            cat = cats[randint(0, longitud - 1)]

            w.category.add(cat)

            w.keywords = self.getParragraph(randint(1, 20), randint(30, 240))
            w.json = json
            w.save()


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
        "ctfRelations": "82.__attribute__outputCTF"
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

#There's no need to bypass manage.py, since it's a wonderful convenience wrapper around
        # the Django project administration tools. It can be used to create custom
        # management commands - e.g. your own commands parallel to shell, dumpdata,
        # and so on. Not only that creating such commands gives you a very succinct,
        # boilterplate-free way of writing custom management scripts, it also gives
        # you a natural location to house them, per application.

