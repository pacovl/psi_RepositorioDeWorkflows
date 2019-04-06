# The name of the script is the name of the custom command,
# so let's call it populate.py.
#
# execute python manage.py populate

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

import django
django.setup()

from application.models import Patient, Doctor, Prescription

#models
PATIENT = 'patient'
DOCTOR = 'doctor'
PRESCRIPTION = 'prescription'

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
        Author: <>
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
