import { useQuery } from '@tanstack/react-query';

import { getDashboardSummary } from './api';


const DashboardSummary = ({
  workspaceSlug
}) => {

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
    return <p>Error: {error.message}</p>;
  }

  return (
    <div>

      <h2>
        {data.workspace}
      </h2>

      <h3>
        Total Events: {data.event_count}
      </h3>

      <h4>Top Pages</h4>

      <ul>
        {data.top_pages.map((page, index) => (
          <li key={index}>
            {page.payload__page}
            {' '}
            -
            {' '}
            {page.view_count}
            {' '}
            views
          </li>
        ))}
      </ul>

    </div>
  );
};

export default DashboardSummary;