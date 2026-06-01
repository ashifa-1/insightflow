# InsightFlow (Multi-Tenant Analytics Dashboard with OAuth, Django, React, Redis, and PostgreSQL)

InsightFlow is a multi-tenant analytics platform built with Django REST Framework, React, PostgreSQL, Redis, and Docker. It allows authenticated users to manage workspaces, ingest analytics events, and view aggregated dashboard insights.

## Features

### Authentication

* Session-based authentication
* Current user endpoint (`/api/auth/me/`)
* Logout endpoint (`/api/auth/logout/`)
* Protected frontend routes

### Multi-Tenant Workspaces

* Create workspaces
* List user workspaces
* Workspace membership-based access control
* Workspace data isolation

### Analytics

* Event ingestion API
* Dashboard summary API
* Dashboard timeseries API
* Top pages aggregation
* Event count tracking

### Performance

* Redis caching for dashboard summaries
* Automatic cache invalidation when new events are created

### Infrastructure

* Dockerized frontend and backend
* PostgreSQL database
* Redis cache
* Environment-based configuration

---

## Tech Stack

### Backend

* Django 5
* Django REST Framework
* PostgreSQL
* Redis
* Docker

### Frontend

* React
* React Router
* React Query
* Vite

---

## Architecture

1. Users authenticate and access the React frontend.
2. The frontend communicates with Django REST APIs.
3. Workspace-level permissions ensure tenant isolation.
4. Analytics events are stored in PostgreSQL.
5. Dashboard queries are cached in Redis.
6. Cache entries are invalidated when new events are ingested.

---

## API Endpoints

### Authentication

#### Get Current User

```http
GET /api/auth/me/
```

#### Logout

```http
POST /api/auth/logout/
```

---

### Workspaces

#### List Workspaces

```http
GET /api/workspaces/
```

#### Create Workspace

```http
POST /api/workspaces/
```

Example Request:

```json
{
  "name": "Acme Corp"
}
```

---

### Analytics

#### Dashboard Summary

```http
GET /api/w/{workspace_slug}/dashboard/summary/
```

Returns:

* Total event count
* Top pages by page views

#### Dashboard Timeseries

```http
GET /api/w/{workspace_slug}/dashboard/timeseries/
```

Optional query parameter:

```http
?period=30d
```

#### Event Ingestion

```http
POST /api/w/{workspace_slug}/events/
```

Example Request:

```json
{
  "event": "page_view",
  "payload": {
    "page": "/pricing"
  }
}
```

---

## Running the Project

### Clone Repository

```bash
git clone https://github.com/ashifa-1/insightflow
cd insightflow
```

### Configure Environment Variables

Create a `.env` file using `.env.example`.

### Start Services

```bash
docker compose up --build
```

### Backend

Available at:

```text
http://localhost:8000
```

### Frontend

Available at:

```text
http://localhost:5173
```

---

## Security

* Workspace-level authorization using custom permissions
* Authenticated access to analytics endpoints
* Multi-tenant data isolation
* Session-based authentication

---

## Future Improvements

* Google OAuth Login
* GitHub OAuth Login
* Advanced analytics dashboards
* Real-time event streaming
* Role-based workspace permissions
