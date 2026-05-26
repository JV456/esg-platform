import FileUploadCard from "../components/FileUploadCard";

import {
  uploadSAPFile,
  uploadUtilityFile,
  uploadTravelFile,
} from "../api/uploadApi";


function UploadPage() {

  return (

    <div className="p-8 bg-gray-100 min-h-screen">

      <h1 className="text-4xl font-bold mb-8">
        ESG Data Uploads
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

        <FileUploadCard
          title="SAP Fuel Data"
          uploadFunction={uploadSAPFile}
        />

        <FileUploadCard
          title="Utility Electricity Data"
          uploadFunction={uploadUtilityFile}
        />

        <FileUploadCard
          title="Travel JSON Data"
          uploadFunction={uploadTravelFile}
        />

      </div>

    </div>
  );
}

export default UploadPage;