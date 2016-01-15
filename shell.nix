with import <nixpkgs> {};

let
pkg = pkgs.python3.buildEnv.override {
    extraLibs = [ (import ./default.nix).imup ];
  };

in
pkg.env