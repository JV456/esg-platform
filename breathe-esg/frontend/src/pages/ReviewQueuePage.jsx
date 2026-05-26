import { useEffect, useState } from "react";

import ReviewTable from "../components/ReviewTable";

import {
  fetchPendingRecords,
  approveRecord,
  rejectRecord,
} from "../api/dashboardApi";


function ReviewQueuePage() {

  const [records, setRecords] = useState([]);

  const loadRecords = async () => {

    try {

      const data = await fetchPendingRecords();

      setRecords(data);

    } catch (error) {

      console.error(error);
    }
  };

  useEffect(() => {
    loadRecords();
  }, []);

  const handleApprove = async (id) => {

    await approveRecord(id);

    loadRecords();
  };

  const handleReject = async (id) => {

    await rejectRecord(id);

    loadRecords();
  };

  return (

    <div className="p-8 bg-gray-100 min-h-screen">

      <h1 className="text-4xl font-bold mb-8">
        Pending Review Queue
      </h1>

      <ReviewTable
        records={records}
        onApprove={handleApprove}
        onReject={handleReject}
      />

    </div>
  );
}

export default ReviewQueuePage;