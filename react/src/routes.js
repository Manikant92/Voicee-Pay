// Material Dashboard 2 React layouts
import Dashboard from "layouts/dashboard";

// @mui icons
import DashboardIcon from "@mui/icons-material/Dashboard";

// icon: <Icon fontSize="small">dashboard</Icon>,
const routes = [
  {
    type: "collapse",
    name: "Dashboard",
    key: "dashboard",
    icon: <DashboardIcon />,
    route: "/dashboard",
    component: <Dashboard />,
  }
];

export default routes;
