import os
import glob
import random
from xoxxox.shared import Custom

#---------------------------------------------------------------------------

class TtsPrc():

  def __init__(self, config="xoxxox/config_ttsply_000", **dicprm):
    diccnf = Custom.update(config, dicprm)
    self.dicdir = {}
    self.lstdir = {}
    self.posdir = {}

  def status(self, config="xoxxox/config_ttsply_000", **dicprm):
    diccnf = Custom.update(config, dicprm)
    if self.dicdir != diccnf["dicdir"]:
      self.dicdir = diccnf["dicdir"]
      self.output = diccnf["output"]
      self.strext = diccnf["strext"]
      for keydir in self.dicdir.keys():
        ptnpth = self.dicdir[keydir] + "/" + "*" + self.strext
        #print(ptnpth, flush=True) # DBG
        self.lstdir[keydir] = glob.glob(ptnpth)
        #print(self.lstdir[keydir], flush=True) # DBG
        self.posdir[keydir] = 0
        if self.output == "random":
          random.shuffle(self.lstdir[keydir])

  def infere(self, txtreq):
    keydir = txtreq
    try:
      p = self.dicdir[keydir]
    except:
      keydir = next(iter(self.dicdir))
    if self.posdir[keydir] >= len(self.lstdir[keydir]):
      self.posdir[keydir] = 0
      if self.output == "random":
        random.shuffle(self.lstdir[keydir])
    dirtgt = self.lstdir[keydir][self.posdir[keydir]]
    with open(dirtgt, "rb") as f:
      datwav = f.read()
    self.posdir[keydir] = self.posdir[keydir] + 1
    return datwav
