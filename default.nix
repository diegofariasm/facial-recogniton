{ pkgs ? import <nixpkgs> { } }:
let
  attendanceSystemEnv = pkgs.poetry2nix.mkPoetryEnv {
    projectDir = ./.;
  };
in
attendanceSystemEnv.env.overrideAttrs (oldAttrs: {
  buildInputs = [
    pkgs.hello
  ];
})
