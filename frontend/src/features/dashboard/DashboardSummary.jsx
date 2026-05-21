import { useQuery } from '@tanstack/react-query';
import { getDashboardSummary } from './api';
import PageViewsChart from './PageViewsChart';
import { useAuth } from '../auth/AuthContext';

const DashboardSummary = ({
  workspaceSlug
}) => {

  const { logout } = useAuth();

  const {
    data,
    isLoading,
    isError,
    error
  } = useQuery({

    queryKey: [
      'dashboardSummary',
      workspaceSlug
    ],

    queryFn: () =>
      getDashboardSummary(workspaceSlug),
  });

  if (isLoading) {
    return <p>Loading summary...</p>;
  }

  if (isError) {
    return (
      <p>
        Error:
        {' '}
        {error.message}
      </p>
    );
  }

  return (

    <div className="stats-card">

      <div className="dashboard-header">

        <h2>
          {data.workspace}
        </h2>

        <button
          className="logout-btn"
          onClick={logout}
        >
          Logout
        </button>

      </div>

      <h3>
        Total Events:
        {' '}
        {data.event_count}
      </h3>

      <div className="top-pages">

        <h4>
          Top Pages
        </h4>

        <ul>

          {data.top_pages.map(
            (page, index) => (

              <li key={index}>

                {page.payload__page}

                {' '}
                -

                {' '}
                {page.view_count}

                {' '}
                views

              </li>
            )
          )}

        </ul>
        <PageViewsChart
          data={data.top_pages}
        />

      </div>

    </div>
  );
};

export default DashboardSummary;
