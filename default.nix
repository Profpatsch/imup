with import <nixpkgs> {};
with pkgs.python3Packages;
{
imup = buildPythonPackage rec {
  name = "imup-${rev}";
  rev = "0.2.5a";

  doCheck = false;
  /*src = pkgs.fetchFromGitHub {
      owner = "Profpatsch";
      repo = "imup";
      inherit rev;
      sha256 = "1c9ysyz16j92kszw4iayqyc8j501la2iv6fwyfkm8i9flawbpdgw";
  };*/
  src = ./.;
  propagatedBuildInputs = [ requests2 ];

};
}