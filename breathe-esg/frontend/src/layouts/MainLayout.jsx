import { Link } from "react-router-dom";

function MainLayout({ children }) {

  return (

    <div>

      <nav className="bg-black text-white p-4 flex gap-6">

        <Link to="/">
          Dashboard
        </Link>

        <Link to="/uploads">
          Uploads
        </Link>

        <Link to="/reviews">
          Review Queue
        </Link>

      </nav>

      {children}

    </div>
  );
}

export default MainLayout;