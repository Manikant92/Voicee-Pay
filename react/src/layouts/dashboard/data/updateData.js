import { useEffect } from "react";
import { useQuery } from "@apollo/client";
import { GET_TOTAL_TRANSACTIONS } from "components/GraphQL";
import { GET_TOTAL_USSD_SESSIONS } from "components/GraphQL";
import { constructGraphData, GetTotalPayments } from "./utils";
import { transactionTemplateData, ussdTemplateData } from "./templateChatData";

function UpdateTransaction(
  setTotalTransaction,
  setTotalTransactionGraphData,
  setTotalPayment
) {
  const { data } = useQuery(GET_TOTAL_TRANSACTIONS, {
    fetchPolicy: "network-only",
  });

  useEffect(() => {
    if (data) {
      console.log("Received transactions - setting the values");
      console.log("Total Transactions - ", data.transactions);
      setTotalTransaction(data.transactions.length);
      setTotalPayment(GetTotalPayments(data.transactions));
      var tempTransactionTemplateData = UpdateGraphData(
        data.transactions,
        setTotalTransactionGraphData,
        false
      );
      console.log("Transaction Graph Data", tempTransactionTemplateData);
    }
  }, [data]);
}

function UpdateUssdSession(
  setTotalUssdSession,
  setTotalUssdSessionGraphData,
  setTotalUssdSessionList
) {
  const { data } = useQuery(GET_TOTAL_USSD_SESSIONS, {
    fetchPolicy: "network-only",
  });

  useEffect(() => {
    if (data) {
      console.log("Received USSD Session - setting the values");
      console.log("Total USSD Sessions - ", data.ussdSessions);
      setTotalUssdSessionList(data.ussdSessions);
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
