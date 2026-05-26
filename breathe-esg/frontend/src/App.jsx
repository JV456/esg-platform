import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

import DashboardPage from "./pages/DashboardPage";
import ReviewQueuePage from "./pages/ReviewQueuePage";
import UploadPage from "./pages/UploadPage";

function App() {

  return (

    <BrowserRouter>

      <MainLayout>

        <Routes>

          <Route
            path="/"
            element={<DashboardPage />}
          />

          <Route
            path="/uploads"
            element={<UploadPage />}
          />

          <Route
            path="/reviews"
            element={<ReviewQueuePage />}
          />

        </Routes>

      </MainLayout>

    </BrowserRouter>
  );
}

export default App;