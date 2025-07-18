import pytest
from django.urls import reverse
from todos.models import Task

@pytest.mark.django_db
def test_task_list_view(client):
    url = reverse('task_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'tasks' in response.context

@pytest.mark.django_db
def test_task_create_and_update(client):
    # Create a new task
    task = Task.objects.create(title='Test Task', completed=False)
    assert Task.objects.count() == 1
    # Update the task
    url = reverse('task_update', args=[task.pk])
    response = client.post(url, {'title': 'Updated Task', 'completed': True})
    task.refresh_from_db()
    assert task.title == 'Updated Task'
    assert task.completed is True

@pytest.mark.django_db
def test_task_completed_view(client):
    task = Task.objects.create(title='Complete Me', completed=False)
    url = reverse('task_completed', args=[task.pk])
    response = client.post(url)
    task.refresh_from_db()
    assert task.completed is True
