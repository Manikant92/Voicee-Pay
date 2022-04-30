import { useEffect } from "react";
import { useQuery } from "@apollo/client";
import { GET_TOTAL_TRANSACTIONS } from "components/GraphQL";
import { GET_TOTAL_USSD_SESSIONS } from "components/GraphQL";
import { constructGraphData, GetTotalPayments, log } from "./utils";
import { transactionTemplateData, ussdTemplateData } from "./templateChatData";

function UpdateTransaction(
  setTotalTransaction,
  setTotalTransactionGraphData,
  setTotalPayment,
  dataFetchToggle
) {
  const { data } = useQuery(GET_TOTAL_TRANSACTIONS, {
    fetchPolicy: "network-only",
    pollInterval: 5000,
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
      UpdateGraphData(data.transactions, setTotalTransactionGraphData, false);
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
    pollInterval: 5000,
    skip: !dataFetchToggle,
  });

  useEffect(() => {
    if (data) {
      log("Received USSD Session - setting the values");
      // log("Total USSD Sessions - ", data.ussdSessions);
      // setTotalUssdSessionList(data.ussdSessions);
      setTotalUssdSession(data.ussdSessions.length);
      UpdateGraphData(data.ussdSessions, setTotalUssdSessionGraphData, true);
    }
  }, [data]);
}

function UpdateGraphData(dataList, setDataList, ussd = true) {
  var tempUssdTemplateData = ussd ? ussdTemplateData : transactionTemplateData;
  if (dataList) {
    tempUssdTemplateData.datasets.data = constructGraphData(dataList);
    setDataList(tempUssdTemplateData);
  }
  return tempUssdTemplateData;
}

export { UpdateTransaction, UpdateUssdSession, UpdateGraphData };