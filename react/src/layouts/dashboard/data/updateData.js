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
      var tempTransactionTemplateData = transactionTemplateData;
      tempTransactionTemplateData.datasets.data = constructGraphData(
        data.transactions
      );
      setTotalTransactionGraphData(tempTransactionTemplateData);
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
      var tempUssdTemplateData = ussdTemplateData;
      tempUssdTemplateData.datasets.data = constructGraphData(
        data.ussdSessions
      );
      setTotalUssdSessionGraphData(tempUssdTemplateData);
    }
  }, [data]);
}

function UpdateGraphData(dataList, setDataList) {
  if (dataList) {
    var tempUssdTemplateData = ussdTemplateData;
    tempUssdTemplateData.datasets.data = constructGraphData(
      dataList
    );
    setDataList(tempUssdTemplateData);
  }
}

export { UpdateTransaction, UpdateUssdSession, UpdateGraphData };
