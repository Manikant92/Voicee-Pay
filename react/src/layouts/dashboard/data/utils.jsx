import { GET_TOTAL_CUSTOMERS } from "components/GraphQL";
import { useEffect } from "react";
import { useQuery } from "@apollo/client";
function GetTotalPayments(totalTransactionList) {
  var totalPayment = 0.0;
  for (var transaction in totalTransactionList) {
    totalPayment += parseFloat(totalTransactionList[transaction].amount);
  }
  // log("Total Payments - $", totalPayment);
  return "$" + totalPayment.toString();
}

function GetTotalCustomers(setTotalCustomers) {
  const { data } = useQuery(GET_TOTAL_CUSTOMERS, {
    fetchPolicy: "network-only",
    pollInterval: 5000
  });

  useEffect(() => {
    if (data) {
      log("Received customer details - setting the values");
      setTotalCustomers(data.customers.length);
      // log("Total customers - " + data.customers.length);
    }
  }, [data]);
}

function constructGraphData(dataList) {
  let weekCountList = [0,0,0,0,0,0,0];

  for (var transaction in dataList) {
    
    let transactionDate = new Date(dataList[transaction].createdAt);
    weekCountList[transactionDate.getDay()] += 1;
  }
  // log("Week days list - ", weekCountList);
  return weekCountList;
}

const log = (...args) =>
  console.log(`[${new Date().toUTCString()}]`, " | Voicee Pay | ", ...args);


export { GetTotalPayments, GetTotalCustomers, constructGraphData, log };
