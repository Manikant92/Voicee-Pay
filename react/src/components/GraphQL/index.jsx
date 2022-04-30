import { gql } from "@apollo/client";

const GET_TOTAL_TRANSACTIONS = gql`
  {
    transactions {
      id
      createdAt
      amount
    }
  }
`;

const GET_TOTAL_USSD_SESSIONS = gql`
  query GetUssdSessions {
    ussdSessions {
      id
      createdAt
    }
  }
`;

const GET_TOTAL_CUSTOMERS = gql`
  {
    customers {
      id
      name
      email
      isActive
    }
  }
`;


export { GET_TOTAL_TRANSACTIONS, GET_TOTAL_USSD_SESSIONS, GET_TOTAL_CUSTOMERS };