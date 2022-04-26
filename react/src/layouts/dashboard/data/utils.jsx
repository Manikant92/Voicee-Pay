import { GET_TOTAL_CUSTOMERS } from "components/GraphQL";
import { useEffect } from "react";
import { useQuery } from "@apollo/client";
function GetTotalPayments(totalTransactionList) {
  var totalPayment = 0.0;
  for (var transaction in totalTransactionList) {
    totalPayment += parseFloat(totalTransactionList[transaction].amount);
  }
  console.log("Total Payments - $", totalPayment);
  return "$" + totalPayment.toString();
}

function GetTotalCustomers(setTotalCustomers) {
  const { data } = useQuery(GET_TOTAL_CUSTOMERS, {
    fetchPolicy: "network-only",
  });

  useEffect(() => {
    if (data) {
      console.log("Received customer details - setting the values");
      setTotalCustomers(data.customers.length);
      console.log("Total customers - " + data.customers.length);
    }
  }, [data]);
}

function constructGraphData(dataList) {
  let weekCountList = [0,0,0,0,0,0,0];

  for (var transaction in dataList) {
    
    let transactionDate = new Date(dataList[transaction].createdAt);
    weekCountList[transactionDate.getDay()] += 1;
  }
  console.log("Week days list - ", weekCountList);
  return weekCountList;
}

export { GetTotalPayments, GetTotalCustomers, constructGraphData };
