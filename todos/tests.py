from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoTestCase(TestCase):
    def setUp(self):
        self.todo_text = "Test Todo Item"
        self.todo = Todo.objects.create(title=self.todo_text)

    def test_todo_creation(self):
        """
        Test that a new todo item can be created.
        """
        self.assertEqual(self.todo.title, self.todo_text)

    def test_add_todo_view(self):
        """
        Test the add todo view.
        """
        response = self.client.post(reverse('todos:add'), {'title': 'New Todo Item'})
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a redirect
        self.assertTrue(Todo.objects.filter(title='New Todo Item').exists())

    def test_delete_todo_view(self):
        """
        Test the delete todo view.
        """
        response = self.client.post(reverse('todos:delete', args=(self.todo.id,)))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(title=self.todo_text).exists())

    def test_update_todo_view(self):
        """
        Test the update todo view.
        """
        response = self.client.post(reverse('todos:update', args=(self.todo.id,)), {'isCompleted': 'on'})
        self.assertEqual(response.status_code, 302)
        updated_todo = Todo.objects.get(pk=self.todo.id)
        self.assertTrue(updated_todo.isCompleted)
