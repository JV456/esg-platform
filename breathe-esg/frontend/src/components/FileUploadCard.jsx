import { useState } from "react";


function FileUploadCard({
  title,
  uploadFunction,
}) {

  const [file, setFile] = useState(null);

  const [loading, setLoading] =
    useState(false);

  const [message, setMessage] =
    useState("");


  const handleUpload = async () => {

    if (!file) {
      setMessage("Please select a file.");
      return;
    }

    try {

      setLoading(true);

      setMessage("");

      await uploadFunction(file, 1);

      setMessage(
        "File uploaded successfully!"
      );

      setFile(null);

    } catch (error) {

      console.error(error);

      setMessage(
        "Upload failed."
      );

    } finally {

      setLoading(false);
    }
  };


  return (

    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-2xl font-bold mb-4">
        {title}
      </h2>

      <input
        type="file"
        onChange={(e) =>
          setFile(e.target.files[0])
        }
        className="mb-4"
      />

      <button
        onClick={handleUpload}
        disabled={loading}
        className="bg-black text-white px-6 py-2 rounded"
      >

        {loading
          ? "Uploading..."
          : "Upload"}

      </button>

      {message && (

        <p className="mt-4 text-sm">
          {message}
        </p>

      )}

    </div>
  );
}

export default FileUploadCard;