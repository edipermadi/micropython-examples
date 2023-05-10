# Builtin button interrupt

This example demonstrates how to use interrupt to get the value of builtin button using M5Stack AtomU board. The button is externally pulled up and will be updated via interrupt, however changes detection (released to pressed or vice versa) is implemented via polling every 0.1 second. Whenever changes detected, the latest state will be printed.