var ussdTemplateData = {
  labels: ["M", "T", "W", "T", "F", "S", "S"],
  datasets: {
    label: "USSD Session",
    data: [0, 2, 0, 0, 0, 0, 0],
  },
};

var transactionTemplateData = {
  labels: ["S", "M", "T", "W", "T", "F", "S"],
  datasets: { label: "Transactions", data: [0, 3, 0, 0, 0, 0, 0] },
};

export { ussdTemplateData, transactionTemplateData };
