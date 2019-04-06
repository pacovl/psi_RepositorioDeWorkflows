
from unittest import TestCase
from data.models import Category
from data.models import Workflow as WorkFlow
from data.management.commands.populate import Command, CATEGORY, WORKFLOW

#DO NOT MODIFIED ANYTHING BELOW THIS POINT
#very basic model testing, we just check the new objects exists
class modelsTests(TestCase):
    def setUp(self):
        #populate database
        self.populate = Command()
        self.populate.handle()

    def test_Category(self):
        # They should be 5 categories called
        self.categories = Category.objects.all()
        self.assertEqual(5, len(self.categories))

    def test_Workflow(self):
        # They should be 13 workflows
        workflows = WorkFlow.objects.all()
        self.assertEqual(13, len(workflows))
        for workflow in workflows:
            categories = workflow.category.all()
            self.assertTrue(len(categories)>0)
            category = categories[0]
            try:
                Category.objects.get(slug=category.slug)
            except Category.DoesNotExist:
                self.assertTrue(False, "category: %s does not exist" %
                                category.slug )
            print("checked: %s" % workflow.name)
