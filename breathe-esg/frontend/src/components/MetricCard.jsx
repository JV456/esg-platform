function MetricCard({ title, value }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-gray-500 text-sm mb-2">
        {title}
      </h2>

      <p className="text-3xl font-bold">
        {value}
      </p>
    </div>
  );
}

export default MetricCard;