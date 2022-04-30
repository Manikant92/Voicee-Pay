import { useEffect } from "react";
import { useQuery } from "@apollo/client";
import { GET_TOTAL_TRANSACTIONS } from "components/GraphQL";
import { GET_TOTAL_USSD_SESSIONS } from "components/GraphQL";
import { constructGraphData, GetTotalPayments, log } from "./utils";

const MINUTE_MS = 5000;

function UpdateTransaction(
  setTotalTransaction,
  setTotalTransactionGraphData,
  setTotalPayment,
  dataFetchToggle
) {
  const { data } = useQuery(GET_TOTAL_TRANSACTIONS, {
    fetchPolicy: "network-only",
    pollInterval: MINUTE_MS,
    skip: !dataFetchToggle,
  });

  useEffect(() => {
    if (data) {
      log("Received transactions - setting the values");
      // log("Total Transactions - ", data.transactions);
      setTotalTransaction(data.transactions.length);
      setTotalPayment(GetTotalPayments(data.transactions));
      // setTotalTransactionsList(data.transactions);
      var tempTransactionTemplateData = UpdateGraphData(
        data.transactions,
        setTotalTransactionGraphData,
        false
      );
      // log("Transaction Graph Data", tempTransactionTemplateData);
      // setTotalTransactionGraphData(tempTransactionTemplateData);
    }

  }, [data]);
}

function UpdateUssdSession(
  setTotalUssdSession,
  setTotalUssdSessionGraphData,
  dataFetchToggle
) {
  const { data } = useQuery(GET_TOTAL_USSD_SESSIONS, {
    fetchPolicy: "network-only",
    pollInterval: MINUTE_MS,
    skip: !dataFetchToggle,
  });

  useEffect(() => {
    if (data) {
      log("Received USSD Session - setting the values");
      // log("Total USSD Sessions - ", data.ussdSessions);
      // setTotalUssdSessionList(data.ussdSessions);
      setTotalUssdSession(data.ussdSessions.length);
      var tempUssdTemplateData = UpdateGraphData(data.ussdSessions, setTotalUssdSessionGraphData, true);
      // setTotalUssdSessionGraphData(tempUssdTemplateData);
    }
  }, [data]);
}

function UpdateGraphData(dataList, setDataList, ussd = true) {
  var tempUssdTemplateData = ussd
    ? {
        labels: ["S", "M", "T", "W", "T", "F", "S"],
        datasets: {
          label: "USSD Session",
          data: [0, 2, 0, 0, 0, 0, 0],
        },
      }
    : {
        labels: ["S", "M", "T", "W", "T", "F", "S"],
        datasets: { label: "Transactions", data: [0, 3, 0, 0, 0, 0, 0] },
      };
  if (dataList) {
    tempUssdTemplateData.datasets.data = constructGraphData(dataList);
    setDataList(tempUssdTemplateData);
  }
  return tempUssdTemplateData;
}

export { UpdateTransaction, UpdateUssdSession, UpdateGraphData };