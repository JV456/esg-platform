import apiClient from "./client";

export const fetchDashboardMetrics = async () => {
  const response = await apiClient.get("/review/dashboard/");
  return response.data;
};

export const fetchPendingRecords = async () => {
  const response = await apiClient.get("/review/pending/");
  return response.data;
};

export const fetchFlaggedRecords = async () => {
  const response = await apiClient.get("/review/flagged/");
  return response.data;
};

export const approveRecord = async (recordId) => {
  const response = await apiClient.post(
    `/review/approve/${recordId}/`
  );

  return response.data;
};

export const rejectRecord = async (recordId) => {
  const response = await apiClient.post(
    `/review/reject/${recordId}/`
  );

  return response.data;
};