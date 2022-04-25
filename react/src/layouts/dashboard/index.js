import React, { useState, useEffect } from "react";
// @mui material components
import Grid from "@mui/material/Grid";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";

// Material Dashboard 2 React example components
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";
import ReportsBarChart from "examples/Charts/BarCharts/ReportsBarChart";
import ReportsLineChart from "examples/Charts/LineCharts/ReportsLineChart";
import ComplexStatisticsCard from "examples/Cards/StatisticsCards/ComplexStatisticsCard";

// Data
import reportsBarChartData from "layouts/dashboard/data/reportsBarChartData";
import reportsLineChartData from "layouts/dashboard/data/reportsLineChartData";

//icons
import PaidIcon from "@mui/icons-material/Paid";
import PhoneIphoneIcon from "@mui/icons-material/PhoneIphone";
import PaymentsIcon from "@mui/icons-material/Payments";
import PeopleAltIcon from "@mui/icons-material/PeopleAlt";

import { useQuery } from "@apollo/client";
import { GET_TOTAL_TRANSACTIONS } from "components/GraphQL";

function Dashboard() {
  const { sales, tasks } = reportsLineChartData;

  const { error, loading, data } = useQuery(GET_TOTAL_TRANSACTIONS, {
    fetchPolicy: "network-only",
  });
  const [totalTransaction, setTotalTransaction] = useState(null);
  const [totalTransactionList, setTotalTransactionList] = useState(null);

  useEffect(() => {
    if (data) {
      console.log("Received transactions - setting the values");
      setTotalTransactionList(data.transactions);
      setTotalTransaction(data.transactions.length);
    
    }
  }, [data]);

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <MDBox py={3}>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6} lg={3}>
            <MDBox mb={1.5}>
              <ComplexStatisticsCard
                color="dark"
                icon={<PaidIcon />}
                title="Transactions"
                count={totalTransaction}
              />
            </MDBox>
          </Grid>
          <Grid item xs={12} md={6} lg={3}>
            <MDBox mb={1.5}>
              <ComplexStatisticsCard
                icon={<PhoneIphoneIcon />}
                title="USSD Session"
                count="108"
              />
            </MDBox>
          </Grid>
          <Grid item xs={12} md={6} lg={3}>
            <MDBox mb={1.5}>
              <ComplexStatisticsCard
                color="success"
                icon={<PaymentsIcon />}
                title="Total Payments"
                count="$34k"
              />
            </MDBox>
          </Grid>
          <Grid item xs={12} md={6} lg={3}>
            <MDBox mb={1.5}>
              <ComplexStatisticsCard
                color="primary"
                icon={<PeopleAltIcon />}
                title="Customers"
                count="7"
              />
            </MDBox>
          </Grid>
        </Grid>
        <MDBox mt={4.5}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={6} lg={6}>
              <MDBox mb={3}>
                <ReportsBarChart
                  color="dark"
                  title="Transactions"
                  description=""
                  date="campaign sent 2 days ago"
                  chart={reportsBarChartData}
                />
              </MDBox>
            </Grid>
            <Grid item xs={12} md={6} lg={6}>
              <MDBox mb={3}>
                <ReportsLineChart
                  color="info"
                  title="USSD Sessions"
                  description=""
                  date="updated 4 min ago"
                  chart={sales}
                />
              </MDBox>
            </Grid>
            {/* <Grid item xs={12} md={6} lg={4}>
              <MDBox mb={3}>
                <ReportsLineChart
                  color="success"
                  title="Payment Requests"
                  description=""
                  date="just updated"
                  chart={tasks}
                />
              </MDBox>
            </Grid> */}
          </Grid>
        </MDBox>
      </MDBox>
      <Footer />
    </DashboardLayout>
  );
}

export default Dashboard;
