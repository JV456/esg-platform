import apiClient from "./client";


export const uploadSAPFile = async (
  file,
  organizationId
) => {

  const formData = new FormData();

  formData.append("file", file);

  formData.append(
    "organization_id",
    organizationId
  );

  const response = await apiClient.post(
    "/ingestion/upload/sap/",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};


export const uploadUtilityFile = async (
  file,
  organizationId
) => {

  const formData = new FormData();

  formData.append("file", file);

  formData.append(
    "organization_id",
    organizationId
  );

  const response = await apiClient.post(
    "/ingestion/upload/utility/",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};


export const uploadTravelFile = async (
  file,
  organizationId
) => {

  const formData = new FormData();

  formData.append("file", file);

  formData.append(
    "organization_id",
    organizationId
  );

  const response = await apiClient.post(
    "/ingestion/upload/travel/",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};