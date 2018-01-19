# Tasks API

This project was generated on Python Flask Framework

## Server

Run `python app.py` for a dev server. Navigate to `http://localhost:5000/`.

## Routes

The project is deployed on heroku with the base link: `https://fltasks.herokuapp.com`

1. `GET /todo` - Get all the tasks
2. `POST /todo` - Add a new task
3. `DELETE /todo/<id>` - Delete a task

The Task object has the following definition

```json
{
  id: number,
  title: string,
  complete: boolean //to check task is complete or not
}
```