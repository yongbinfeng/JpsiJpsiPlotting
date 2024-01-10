from CMSPLOTS.myFunction import DrawHistos
import ROOT

ROOT.gROOT.SetBatch(True)

# change this input address
finput = "../myhbk.root"

f = ROOT.TFile(finput)

hname = "myFourMuonmass"
h = f.Get(hname)
h.SetLineColor(1)
h.SetMarkerStyle(20)

DrawHistos([h], ["Data"], 6, 10, "m(#mu^{+}#mu^{-}#mu^{+}#mu^{-}) [GeV/c^{2}]", 0, 50, "Events / (0.1 GeV/c^{2})", outputname = "fourmuon_mass", dology=False, legendoptions=["ep"], nMaxDigits=3)

hname1 = "myDiMuon1mass"
hname2 = "myDiMuon2mass"

h1 = f.Get(hname1)
h2 = f.Get(hname2)
h1.SetLineColor(1)
h1.SetMarkerColor(1)
h1.SetMarkerStyle(20)
h2.SetLineColor(2)
h2.SetMarkerColor(2)
h2.SetMarkerStyle(20)
DrawHistos([h1, h2], ["1st J/psi", "2nd J/psi"], 2.5, 3.5, "m(#mu^{+}#mu^{-}) [GeV/c^{2}]", 0, 2000, "Events / (0.1 GeV/c^{2})", outputname = "dimuon_mass", dology=False, legendoptions=["ep", "ep"], addOverflow=True, addUnderflow=True, nMaxDigits=3)