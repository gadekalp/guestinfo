#!/bin/sh

if [ -n "${VMX_GUESTINFO}" ]; then
  if [ -n "${VMX_GUESTINFO_METADATA}" ] || \
     [ -n "${VMX_GUESTINFO_USERDATA}" ] || \
     [ -n "${VMX_GUESTINFO_VENDORDATA}" ]; then
     exit 0
  fi
fi

if ! command -v xenstore-read >/dev/null 2>&1; then
  exit 1
fi

if { xenstore-read "vm-data/metadata" || \
     xenstore-read "vm-data/userdata" || \
     xenstore-read "vm-data/vendordata"; } >/dev/null 2>&1; then
   exit 0
fi

exit 1
