import { useEffect, useState } from "react";

import MetricCard from "../components/MetricCard";

import {
  fetchDashboardMetrics,
} from "../api/dashboardApi";


function DashboardPage() {

  const [metrics, setMetrics] = useState(null);

  useEffect(() => {

    const loadMetrics = async () => {

      try {

        const data = await fetchDashboardMetrics();

        setMetrics(data);

      } catch (error) {

        console.error(error);
      }
    };

    loadMetrics();

  }, []);

  if (!metrics) {
    return <div className="p-10">Loading...</div>;
  }

  return (

    <div className="p-8 bg-gray-100 min-h-screen">

      <h1 className="text-4xl font-bold mb-8">
        ESG Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

        <MetricCard
          title="Total Records"
          value={metrics.total_records}
        />

        <MetricCard
          title="Pending Reviews"
          value={metrics.pending_reviews}
        />

        <MetricCard
          title="Approved Records"
          value={metrics.approved_records}
        />

        <MetricCard
          title="Rejected Records"
          value={metrics.rejected_records}
        />

        <MetricCard
          title="Flagged Records"
          value={metrics.flagged_records}
        />

      </div>
    </div>
  );
}

export default DashboardPage;