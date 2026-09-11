# Multiconductor AC power flow in the browser with tellegen

Solve the IEEE 13 node test feeder, three-phase and unbalanced, with nothing installed.
You need a current browser and the two files in this folder.

## Files

- `ieee13.bmopf.json`: IEEE 13 in draft BMOPF 0.2 JSON, converted from the OpenDSS
  distribution's `IEEE13Nodeckt.dss` with PowerIO 0.11.1
  (`powerio convert IEEE13Nodeckt.dss --to bmopf-json -o ieee13.bmopf.json`).
- `ieee13.geo.json`: the published bus layout from `IEEE13Node_BusXY.csv` as a GeoJSON
  `FeatureCollection`: one `Point` per bus (`properties.bus`), one `LineString` per line,
  switch, and transformer (`properties.bus_from`, `bus_to`), and
  `"powerio_geo": {"space": "diagram"}` because these are drawing coordinates, not
  longitude and latitude. 16 buses, 19 routes.
- `NOTICE-OPENDSS-BSD-3-CLAUSE`: license of the source feeder data.

## Steps

1. Open <https://tellegen.dev>.
2. Drag `ieee13.bmopf.json` onto the page, or use **drop a case file** in the header.
   PowerIO, compiled to WebAssembly, classifies the JSON by content and opens the
   multiconductor viewer. The file stays on your device; nothing is uploaded.
3. Drag `ieee13.geo.json` onto the page. The case panel reports how many buses and routes
   matched and draws the feeder in its published layout. Without a layer, tellegen draws a
   generated tree diagram.
4. Open **Studies**. The panel reads **Distribution power flow**. Choose **Run power flow**.
   The network panel's **Solve AC power flow** button runs the same calculation.
5. Read the summary: status, iterations and time, voltage band, load voltage range, source
   P and Q in kW and kvar, and passive loss in kW. Select a bus for each terminal's voltage
   to ground in volts and degrees, including the neutral. Select a branch for conductor
   currents in amperes and terminal powers.
6. **Save result** keeps the study in this browser; **Export** downloads a snapshot;
   **Download geography** writes the current layout back out as a `.geo.json` layer.

## What the solver does and does not do

The solver is a fixed-point iteration around one sparse complex LU factorization. It updates
compensated load currents until both voltage changes and KCL residuals meet tolerance, and
reports convergence and voltage validity separately.

Supported: constant power, constant current, constant impedance, ZIP, and exponential loads;
two-winding transformers; fixed-tap single-phase autotransformer regulators (IEEE 13 and 34
regulators keep their BMOPF taps).

Not supported today: multiconductor AC OPF, regulator and inverter controls, generator or
inverter injections, finite source impedance, transformers with more than two windings. Raw
OpenDSS `.dss` files open view-only; convert them to BMOPF first.

## Bring your own feeder

```
cargo install powerio-cli
powerio convert my_feeder.dss --to bmopf-json -o my_feeder.bmopf.json
```

The writer reports every field the BMOPF schema cannot hold. To place a feeder on the map
instead of a diagram, write `"powerio_geo": {"space": "geographic"}` and give coordinates as
`[longitude, latitude]`.

## Provenance

The IEEE 13 node test feeder ships with the OpenDSS distribution (EPRI, BSD 3-Clause; see the
notice file) and was converted unchanged. Draft BMOPF 0.2 remains subject to Task Force
review. The steps follow tellegen's documentation for the build deployed on September 11,
2026, which carries the Run power flow controls; the case file was converted with the same
PowerIO version that build uses.
