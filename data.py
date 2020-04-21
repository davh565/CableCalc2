from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Table14(Base):
    __tablename__ = 'TABLE14'
    SIZE = Column(Float, primary_key=True)
    UNENC_SPACED_CU_SOLID = Column(Integer)
    UNENC_SPACED_CU_FLEX = Column(Integer)
    UNENC_SPACED_AL = Column(Integer)
    UNENC_TOUCHING_CU_SOLID = Column(Integer)
    UNENC_TOUCHING_CU_FLEX = Column(Integer)
    UNENC_TOUCHING_AL = Column(Integer)
    UNENC_EXPOSED_CU_SOLID = Column(Integer)
    UNENC_EXPOSED_CU_FLEX = Column(Integer)
    UNENC_EXPOSED_AL = Column(Integer)
    ENC_IN_AIR_CU_SOLID = Column(Integer)
    ENC_IN_AIR_FLEX = Column(Integer)
    ENC_IN_AIR_AL = Column(Integer)
    UNENC_PARTIAL_CU = Column(Integer)
    UNENC_PARTIAL_AL = Column(Integer)
    ENC_PARTIAL_CU = Column(Integer)
    ENC_PARTIAL_AL = Column(Integer)
    UNENC_COMPLETE_CU = Column(Integer)
    UNENC_COMPLETE_AL = Column(Integer)
    ENC_COMPLETE_CU = Column(Integer)
    ENC_COMPLETE_AL = Column(Integer)
    BURIED_DIRECT_CU = Column(Integer)
    BURIED_DIRECT_AL = Column(Integer)
    UNDERGROUND_ENC_CU_SOLID = Column(Integer)
    UNDERGROUND_ENC_CU_FLEX = Column(Integer)
    UNDERGROUND_ENC_AL = Column(Integer)

    def __str__(self):
        return "<TABLE14> {0}mm^2, {1}A".format(self.SIZE, self.UNENC_SPACED_CU_SOLID)


class CableCalculation(Base):
    __tablename__ = 'cable_calculations'
    # primary key: NAME
    NAME = Column(String, primary_key=True)
    LOAD_KW = Column(Float, default=0.0)
    LOAD_AMPS = Column(Float, default=0.0)
    CABLE_LENGTH = Column(Float, default=0.0)
    LOAD_TYPE = Column(String, default="")
    INSTALL_METHOD = Column(String, default="")

    def __str__(self):
        return "<CableCalculation> {0}, {1}m".format(self.NAME, self.CABLE_LENGTH)


class InstallMethod(Base):
    __tablename__ = 'install_methods'
    # primary key: NAME
    NAME = Column(String, primary_key=True)

    def __str__(self):
        return "<InstallMethod> {0}".format(self.NAME)


class SystemParameter(Base):
    __tablename__ = 'system_parameters'
    # primary key: NAME
    NAME = Column(String, primary_key=True)
    VALUE = Column(Float, default=0.0)

    def __str__(self):
        return "<SystemParameter> {0}: {1}".format(self.NAME, self.VALUE)
