import { useEffect } from "react";
import { useQuery } from "@apollo/client";
import { GET_TOTAL_TRANSACTIONS } from "components/GraphQL";
import { GET_TOTAL_USSD_SESSIONS } from "components/GraphQL";
import {GetTotalPayments} from "./utils";

function UpdateTransaction(
  setTotalTransaction,
  setTotalTransactionList,
  setTotalPayment
) {
  const { data } = useQuery(GET_TOTAL_TRANSACTIONS, {
    fetchPolicy: "network-only",
  });

  useEffect(() => {
    if (data) {
      console.log("Received transactions - setting the values");
      setTotalTransactionList(data.transactions);
      setTotalTransaction(data.transactions.length);
      setTotalPayment(GetTotalPayments(data.transactions));
    }
  }, [data]);
}

function UpdateUssdSession(setTotalUssdSession, setTotalUssdSessionList) {
  const { data } = useQuery(GET_TOTAL_USSD_SESSIONS, {
    fetchPolicy: "network-only",
  });

  useEffect(() => {
    if (data) {
      console.log("Received USSD Session - setting the values");
      setTotalUssdSessionList(data.ussdSessions);
      setTotalUssdSession(data.ussdSessions.length);
    }
  }, [data]);
}

export { UpdateTransaction, UpdateUssdSession };
