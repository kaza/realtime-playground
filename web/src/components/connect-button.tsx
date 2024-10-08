"use client";

import { useState, useEffect, useCallback } from "react";
import { Button } from "@/components/ui/button";
import { useConnection } from "@/hooks/use-connection";
import { Loader2, Mic } from "lucide-react";
import { usePlaygroundState } from "@/hooks/use-playground-state";
import { AuthDialog } from "./auth";

export function ConnectButton() {
  const { connect, disconnect, shouldConnect } = useConnection();
  const [connecting, setConnecting] = useState<boolean>(false);

  const handleConnectionToggle = async () => {
    if (shouldConnect) {
      await disconnect();
    } else {
      await initiateConnection();
    }
  };

  const initiateConnection = useCallback(async () => {
    setConnecting(true);
    try {
      await connect();
    } catch (error) {
      console.error("Connection failed:", error);
    } finally {
      setConnecting(false);
    }
  }, [connect]);

  return (
    <Button
      onClick={handleConnectionToggle}
      disabled={connecting || shouldConnect}
      className="text-sm font-semibold bg-oai-green"
    >
      {connecting || shouldConnect ? (
        <>
          <Loader2 className="mr-2 h-4 w-4 animate-spin" />
          Connecting
        </>
      ) : (
        <>
          <Mic className="mr-2 h-4 w-4" />
          Connect
        </>
      )}
    </Button>
  );
}
