import * as React from "react";
import ToggleButton from "@mui/material/ToggleButton";
import UpdateIcon from "@mui/icons-material/Update";

export default function StandaloneToggleButton() {
  const [selected, setSelected] = React.useState(false);

  return (
    <ToggleButton
      value="check"
      selected={selected}
      color="success"
      onChange={() => {
        setSelected(!selected);
      }}
    >
      <UpdateIcon fontSize="medium" />
    </ToggleButton>
  );
}
