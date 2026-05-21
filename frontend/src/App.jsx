import {
  BrowserRouter,
  Routes,
  Route
} from 'react-router-dom';

import {
  useState
} from 'react';

import DashboardSummary from './features/dashboard/DashboardSummary';

import ProtectedRoute from './components/ProtectedRoute';

import LoginPage from './pages/LoginPage';


function DashboardPage() {

  const [
    workspaceSlug,
    setWorkspaceSlug
  ] = useState('insightflow');

  return (

    <div className="container">

      <div className="dashboard-header">

        <h1>
          InsightFlow Dashboard
        </h1>

        <select
          className="workspace-select"
          value={workspaceSlug}
          onChange={(e) =>
            setWorkspaceSlug(
              e.target.value
            )
          }
        >

          <option value="insightflow">
            InsightFlow Analytics
          </option>

          <option value="acme">
            Acme Corp
          </option>

        </select>

      </div>

      <DashboardSummary
        workspaceSlug={workspaceSlug}
      />

    </div>
  );
}


function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route
          path="/login"
          element={<LoginPage />}
        />

        <Route
          path="/"
          element={
            <ProtectedRoute>

              <DashboardPage />

            </ProtectedRoute>
          }
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;