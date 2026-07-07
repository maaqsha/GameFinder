export const manifest = {
  screens: {
    scr_53pk7v: { name: "Home", route: "/", position: { "x": 160, "y": 220 } },
    scr_3lnlxf: { name: "Recommendation", route: "/recommendation", position: { "x": 1560, "y": 220 } },
    scr_7ame3b: { name: "Results", route: "/results", position: { "x": 2960, "y": 220 } },
    scr_82hu40: { name: "Game Detail", route: "/game/6", position: { "x": 4360, "y": 220 } }
  },
  sections: {
    sec_ugtbiy: { name: "Game Discovery Flow", x: 0, y: 0, width: 5720, height: 1180 }
  },
  layers: [
  { kind: "section", id: "sec_ugtbiy", children: [
    { kind: "screen", id: "scr_53pk7v" },
    { kind: "screen", id: "scr_3lnlxf" },
    { kind: "screen", id: "scr_7ame3b" },
    { kind: "screen", id: "scr_82hu40" }]
  }]

};