# -*- coding: utf-8 -*-
import sys
import tkinter as tk

class ScrollerFrame(tk.Frame):

    def __init__(self,parent,activeMouseWheel=True,*args,**kw):
        if sys.version_info < (3,):
            tk.Frame.__init__(self, parent,*args,**kw)
        else:
            super(ScrollerFrame, self).__init__(parent,*args,**kw)
        self.pack(expand=tk.TRUE,fill=tk.BOTH)
        self.parent = parent
        self.ysBar = tk.Scrollbar(self,orient=tk.VERTICAL)
        self.ysBar.pack(side=tk.RIGHT,expand=tk.FALSE,fill=tk.Y)
        self.canv = tk.Canvas(self,bd=0,highlightthickness=0,yscrollcommand=self.ysBar.set)
        self.canv.pack(side=tk.LEFT,expand=tk.TRUE,fill=tk.BOTH)
        self.ysBar.config(command=self.canv.yview)
        self.canv.yview_moveto(0)
        self.canv.xview_moveto(0)
        self.interior = interior = tk.Frame(self.canv)
        interior_id = self.canv.create_window(0,0,window=interior,anchor=tk.NW)

        def _configure_interior(event):
            size = (interior.winfo_reqwidth(),interior.winfo_reqheight())
            self.canv.config(scrollregion="0 0 %s %s" % size)

            if interior.winfo_reqwidth() != self.canv.winfo_width():
                self.canv.config(width=interior.winfo_reqwidth())

            if interior.winfo_reqheight() != self.canv.winfo_height():
                self.canv.config(height=interior.winfo_reqheight())

        interior.bind('<Configure>',_configure_interior)

        def _on_mousewheel(event):
            self.canv.yview_scroll(int(-1*(event.delta/120)),"units")

        def _bound_to_mousewheel(event):
            self.canv.bind_all("<MouseWheel>",_on_mousewheel)
        if activeMouseWheel == True:
            self.interior.bind('<Enter>',_bound_to_mousewheel)

        def _unbound_to_mousewheel(event):
            self.canv.unbind_all("<MouseWheel>")
        if activeMouseWheel == True:
            self.interior.bind('<Leave>',_unbound_to_mousewheel)

        def _configure_canvas(event):
             if interior.winfo_reqwidth() != self.canv.winfo_width():
                 self.canv.itemconfigure(interior_id,width=self.canv.winfo_width())

        self.canv.bind('<Configure>',_configure_canvas)
        