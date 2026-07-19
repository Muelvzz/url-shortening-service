# URL Shortening Service

**Roadmap SH Link:** https://roadmap.sh/projects/url-shortening-service**

This is an intermediate project from _Roadmap.sh_ website

## Tech Stack

**Server:** FastAPI

**Database**: Supabase

## Features

- CRUD Operations

## Installation

Install url-shortening-service with the following commands

```bash
  git clone https://github.com/Muelvzz/url-shortening-service.git
  cd url-shortening-service
  uv init
  uv pip install -r requirements.txt
  uv sync
```

## How to run this project

To run this project in your local terminal

```bash
  uv run python -m app.main --reload
```

For running the tests

```bash
  uv run python -m pytest
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SUPABASE_PASSWORD`

`SUPABASE_URL`

`SUPABASE_KEY`

## API Reference

#### Get all urls

```http
  GET /url/all
```

#### Get url

```http
  GET /url/{id}
```

| Parameter | Type  | Description                          |
| :-------- | :---- | :----------------------------------- |
| `id`      | `int` | **Required**. Id of the url to fetch |

## Lessons Learned

- **I learned how to use Supabase**: This is my introduction towards using modern databases like Supabase, and I love how easy it is to configure and query in my database over postgres.

- **I learned how to do unit tests using pytest**: Building this project gave me an introduction of how to test my specific functions using pytest.

## Feedback

If you have any feedback or concerns, please reach out to me at my LinkedIn profile, **Muelvin Lopez**
