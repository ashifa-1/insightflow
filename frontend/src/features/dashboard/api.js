import { apiClient } from '../../api/client';

export const getDashboardSummary = async (
  workspaceSlug
) => {

  const { data } = await apiClient.get(
    `/api/w/${workspaceSlug}/dashboard/summary/`
  );

  return data;
};