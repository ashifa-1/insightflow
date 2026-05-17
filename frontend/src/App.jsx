import DashboardSummary from './features/dashboard/DashboardSummary';
function App() {
  return (
    <div>
      <h1>
        InsightFlow Dashboard
      </h1>
      <DashboardSummary
        workspaceSlug="insightflow"
      />
    </div>
  );
}
export default App;