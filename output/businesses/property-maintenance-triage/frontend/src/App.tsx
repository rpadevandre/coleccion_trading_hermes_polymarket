import React, { useMemo, useState } from 'react';
    import Landing from './views/Landing';
import TenantRequestDemo from './views/TenantRequestDemo';
import ROICalculator from './views/ROICalculator';
import PortfolioAuditForm from './views/PortfolioAuditForm';
import PilotSignup from './views/PilotSignup';
    import { businessMeta } from './businessMeta';
    import './styles.css';

    const routes = {
      'landing': Landing,
  'tenant-request-demo': TenantRequestDemo,
  'r-o-i-calculator': ROICalculator,
  'portfolio-audit-form': PortfolioAuditForm,
  'pilot-signup': PilotSignup,
    };

    export default function App() {
      const [route, setRoute] = useState<keyof typeof routes>('landing');
      const ActiveView = useMemo(() => routes[route], [route]);

      return (
        <div className="app-shell">
          <nav className="top-nav">
            <strong>{businessMeta.name}</strong>
              <button onClick={() => setRoute('landing')} className={route === 'landing' ? 'active' : ''}>Landing</button>
          <button onClick={() => setRoute('tenant-request-demo')} className={route === 'tenant-request-demo' ? 'active' : ''}>TenantRequestDemo</button>
          <button onClick={() => setRoute('r-o-i-calculator')} className={route === 'r-o-i-calculator' ? 'active' : ''}>ROICalculator</button>
          <button onClick={() => setRoute('portfolio-audit-form')} className={route === 'portfolio-audit-form' ? 'active' : ''}>PortfolioAuditForm</button>
          <button onClick={() => setRoute('pilot-signup')} className={route === 'pilot-signup' ? 'active' : ''}>PilotSignup</button>
          </nav>
          <ActiveView />
        </div>
      );
    }
