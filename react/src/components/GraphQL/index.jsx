import { gql } from "@apollo/client";

const GET_TOTAL_TRANSACTIONS = gql`
  {
    transactions {
      createdAt
      amount
    }
  }
`;

const GET_TOTAL_USSD_SESSIONS = gql`
  {
    ussdSessions {
      createdAt
    }
  }
`;

const GET_TOTAL_CUSTOMERS = gql`
  {
    customers {
      name
      email
      isActive
    }
  }
`;


export { GET_TOTAL_TRANSACTIONS, GET_TOTAL_USSD_SESSIONS, GET_TOTAL_CUSTOMERS };