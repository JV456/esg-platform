function ReviewTable({
  records,
  onApprove,
  onReject,
}) {

  return (

    <div className="overflow-x-auto bg-white rounded-xl shadow-md">

      <table className="w-full">

        <thead className="bg-gray-200">

          <tr>

            <th className="p-4 text-left">Activity</th>

            <th className="p-4 text-left">Scope</th>

            <th className="p-4 text-left">Quantity</th>

            <th className="p-4 text-left">Flagged</th>

            <th className="p-4 text-left">Actions</th>

          </tr>

        </thead>

        <tbody>

          {records.map((record) => (

            <tr
              key={record.id}
              className="border-b"
            >

              <td className="p-4">
                {record.activity_type}
              </td>

              <td className="p-4">
                {record.scope}
              </td>

              <td className="p-4">
                {record.quantity}
              </td>

              <td className="p-4">

                {record.is_flagged ? (
                  <span className="text-red-500 font-bold">
                    YES
                  </span>
                ) : (
                  "NO"
                )}

              </td>

              <td className="p-4 flex gap-2">

                <button
                  onClick={() => onApprove(record.id)}
                  className="bg-green-500 text-white px-4 py-2 rounded"
                >
                  Approve
                </button>

                <button
                  onClick={() => onReject(record.id)}
                  className="bg-red-500 text-white px-4 py-2 rounded"
                >
                  Reject
                </button>

              </td>

            </tr>
          ))}

        </tbody>

      </table>
    </div>
  );
}

export default ReviewTable;