from sqlalchemy.orm.exc import FlushError

from data import CableCalculation, InstallMethod, SystemParameter


def load_data(sql_session):
    # load CableCalculation defaults
    try:

        # NAME = Column(String, primary_key=True)
        # LOAD_KW = Column(Float, default=0.0)
        # LOAD_AMPS = Column(Float, default=0.0)
        # CABLE_LENGTH = Column(Float, default=0.0)
        # LOAD_TYPE = Column(String, default="")
        # INSTALL_METHOD = Column(String, default="")

        # add a couple of loads
        sql_session.add(
            CableCalculation(NAME="LOAD1", LOAD_KW=2.5, LOAD_AMPS=0.0, CABLE_LENGTH=30.0, LOAD_TYPE="DOL", INSTALL_METHOD="", ))
        sql_session.add(
            CableCalculation(NAME="LOAD2", LOAD_KW=1.2, LOAD_AMPS=0.0, CABLE_LENGTH=32.0, LOAD_TYPE="VSD", INSTALL_METHOD="", ))

        sql_session.commit()
    except FlushError:
        print("sql-error: invalid CableCalculation data")

    # load InstallMethod defaults
    try:

        # NAME = Column(String, primary_key=True)

        # add a couple of install methods
        sql_session.add(
            InstallMethod(NAME="UNENCLOSED TOUCHING", ))
        sql_session.add(
            InstallMethod(NAME="UNENCLOSED SPACED", ))

        sql_session.commit()
    except FlushError:
        print("sql-error: invalid InstallMethod data")

    # load SystemParameter defaults
    try:

        # NAME = Column(String, primary_key=True)
        # VALUE = Column(String, default="")

        # add some system parameters
        sql_session.add(
            SystemParameter(NAME="PF_DEFAULT", VALUE=0.9))
        sql_session.add(
            SystemParameter(NAME="VOLTAGE_SYSTEM", VALUE=400))
        sql_session.add(
            SystemParameter(NAME="VOLTAGE_PHASE", VALUE=230))
        sql_session.add(
            SystemParameter(NAME="VOLT_DROP_MAX", VALUE=0.05))
        sql_session.add(
            SystemParameter(NAME="CU_CONSTANT", VALUE=0.0225))
        sql_session.add(
            SystemParameter(NAME="AL_CONSTANT", VALUE=0.036))

        sql_session.commit()
    except FlushError:
        print("sql-error: invalid SystemParameter data")
