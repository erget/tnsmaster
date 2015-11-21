from tnsnames.tnsnamesParser import tnsnamesParser
from tnsnames.tnsnamesformatter import TnsnamesFormatter


class TnsnameOraStyleFormatter(TnsnamesFormatter):
    def __init__(self):
        super().__init__()
        self._current_line = ""
        self._level = 0
        self._indents = 4

    def get_indents_string(self):
        ret_string = " " * self._indents * self._level
        return ret_string

    def set_indents(self, indents):
        self._indents = indents

    def append_current_line(self):
        """
           Appends and clears the current line

        """
        self._lines.append(self.get_indents_string() + self._current_line)
        self._current_line = ""

    # Enter a parse tree produced by tnsnamesParser#description_list.
    def enterDescription_list(self, ctx: tnsnamesParser.Description_listContext):
        super().enterDescription_list(ctx)
        self.append_current_line()
        line_string = self.get_indents_string() + "(" + tnsnamesParser.ruleNames[
            tnsnamesParser.RULE_description_list] + "="
        self._level += 1
        self._lines.append(line_string)

    # Exit a parse tree produced by tnsnamesParser#description_list.
    def exitDescription_list(self, ctx: tnsnamesParser.Description_listContext):
        super().exitDescription_list(ctx)
        self._level -= 1
        line_string = self.get_indents_string() + ")"
        self._lines.append(line_string)

    # Enter a parse tree produced by tnsnamesParser#description.
    def enterDescription(self, ctx: tnsnamesParser.DescriptionContext):
        super().enterDescription(ctx)
        line_string = self.get_indents_string() + "(" + tnsnamesParser.ruleNames[
            tnsnamesParser.RULE_description] + "="
        self._level += 1
        self._lines.append(line_string)

    # Exit a parse tree produced by tnsnamesParser#description.
    def exitDescription(self, ctx: tnsnamesParser.DescriptionContext):
        super().exitDescription(ctx)
        self._level -= 1
        line_string = self.get_indents_string() + ")"
        self._lines.append(line_string)

    # Enter a parse tree produced by tnsnamesParser#d_sdu.
    def enterD_sdu(self, ctx: tnsnamesParser.D_sduContext):
        super().enterD_sdu(self)
        self._current_line = ctx.getText()
        self.append_current_line()

    # Enter a parse tree produced by tnsnamesParser#d_conn_timeout.
    def enterD_conn_timeout(self, ctx: tnsnamesParser.D_conn_timeoutContext):
        super().enterD_conn_timeout(ctx)
        self._current_line = ctx.getText()
        self.append_current_line()

    # Exit a parse tree produced by tnsnamesParser#d_conn_timeout.
    def exitD_conn_timeout(self, ctx: tnsnamesParser.D_conn_timeoutContext):
        super().exitD_conn_timeout(ctx)

    # Enter a parse tree produced by tnsnamesParser#d_retry_count.
    def enterD_retry_count(self, ctx: tnsnamesParser.D_retry_countContext):
        super().enterD_retry_count(ctx)
        self._current_line = ctx.getText()
        self.append_current_line()

    # Enter a parse tree produced by tnsnamesParser#address_list.
    def enterAddress_list(self, ctx: tnsnamesParser.Address_listContext):
        super().enterAddress_list(ctx)
        line_string = self.get_indents_string() + "(" + tnsnamesParser.ruleNames[
            tnsnamesParser.RULE_address_list] + "="
        self._level += 1
        self._lines.append(line_string)

    # Exit a parse tree produced by tnsnamesParser#address_list.
    def exitAddress_list(self, ctx: tnsnamesParser.Address_listContext):
        super().exitAddress_list(ctx)
        self._level -= 1
        line_string = self.get_indents_string() + ")"
        self._lines.append(line_string)

    # Enter a parse tree produced by tnsnamesParser#al_load_balance.
    def enterAl_load_balance(self, ctx: tnsnamesParser.Al_load_balanceContext):
        super().enterAl_load_balance(ctx)
        self._current_line = ctx.getText()
        self.append_current_line()

    # Exit a parse tree produced by tnsnamesParser#al_load_balance.
    def exitAl_load_balance(self, ctx: tnsnamesParser.Al_load_balanceContext):
        super().exitAl_load_balance(ctx)

    # Enter a parse tree produced by tnsnamesParser#address.
    def enterAddress(self, ctx: tnsnamesParser.AddressContext):
        super().enterAddress(ctx)
        ret_string = self.get_indents_string() + ctx.getText()
        self._lines.append(ret_string)

    # Exit a parse tree produced by tnsnamesParser#address.
    def exitAddress(self, ctx: tnsnamesParser.AddressContext):
        super().exitAddress(ctx)

    # Enter a parse tree produced by tnsnamesParser#host.
    def enterHost(self, ctx: tnsnamesParser.HostContext):
        # ret_string = self.get_indents_string() + ctx.getRuleContext().parentCtx.getText()
        # self._lines.append(ret_string)
        super().enterHost(ctx)

    # Exit a parse tree produced by tnsnamesParser#host.
    def exitHost(self, ctx: tnsnamesParser.HostContext):
        super().exitHost(ctx)
